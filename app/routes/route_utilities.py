from flask import abort, make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        # response = {"message": f"book {book_id} invalid"}
        abort(make_response({"message": f"{cls.__name__} id {(model_id)} invalid"}, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        # response = {"message": f"model {model_id} not found"}
        abort(make_response({"message": f"{cls.__name__} {(model_id)} not found"}, 400))


    return model