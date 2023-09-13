from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person_database.db'
db = SQLAlchemy(app)


class PersonModel(db.Model):
    __tablename__ = 'person_model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Person(name={self.name}, id={self.id})"


person_update_args = reqparse.RequestParser()
person_update_args.add_argument("name", type=str, help="Name of the person")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
}


class Person(Resource):
    @marshal_with(resource_fields)
    def get(self, person_id_or_name):
        if person_id_or_name.isdigit():
            # If the input is a digit, assume it's an ID
            result = PersonModel.query.filter_by(id=int(person_id_or_name)).first()
        else:
            # Otherwise, assume it's a name
            result = PersonModel.query.filter_by(name=person_id_or_name).first()

        if not result:
            abort(404, message="Person not found")
        return result

    @marshal_with(resource_fields)
    def patch(self, person_id_or_name):
        args = person_update_args.parse_args()

        if person_id_or_name.isdigit():
            result = PersonModel.query.filter_by(id=int(person_id_or_name)).first()
        else:
            result = PersonModel.query.filter_by(name=person_id_or_name).first()

        if not result:
            abort(404, message="Person not found")

        if args['name']:
            # Input validation for name update
            new_name = args['name']
            if not isinstance(new_name, str) or len(new_name) > 100:
                abort(400, message="Invalid 'name' format or length")

            result.name = new_name

        db.session.commit()

        return result, "Person updated successfully"

    def delete(self, person_id_or_name):
        if person_id_or_name.isdigit():
            # If the input is a digit, assume it's an ID
            result = PersonModel.query.filter_by(id=int(person_id_or_name)).first()
        else:
            # Otherwise, assume it's a name
            result = PersonModel.query.filter_by(name=person_id_or_name).first()

        if not result:
            abort(404, message="Person not found")

        db.session.delete(result)
        db.session.commit()
        return '', 204


class PersonWithID(Resource):
    @marshal_with(resource_fields)
    def post(self, person_id):
        args = person_update_args.parse_args()

        # Check if a person with the specified ID already exists
        existing_person = PersonModel.query.filter_by(id=person_id).first()
        if existing_person:
            abort(409, message=f"A person with ID {person_id} already exists")

        # Input validation: Ensure 'name' is a string and not too long
        name = args['name']
        if not isinstance(name, str) or len(name) > 100:
            abort(400, message="Invalid 'name' format or length")

        person = PersonModel(id=person_id, name=name)
        db.session.add(person)
        db.session.commit()
        return person, 201


#  routes for retrieving (GET), updating (PATCH), and deleting (DELETE) persons
api.add_resource(Person, "/api/<person_id_or_name>")
#  route for POST operation with a specified ID
api.add_resource(PersonWithID, "/api/<int:person_id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
