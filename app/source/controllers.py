from flask import Blueprint,jsonify
from source import db
from source.models import EmailJson
from source.atf_email_parsing import ATFEmail

flaskpoc = Blueprint('atf', __name__, url_prefix='/')

@flaskpoc.route('/')
def hello():
    return "Hello ATF!"

@flaskpoc.route('/json')
def email_json():
    try:
        atfemail = ATFEmail()
        fetched_data = atfemail.email_data()
        html_data = fetched_data["html"]
        return html_data
    except Exception as e:
        return(str(e))

@flaskpoc.route('/add')
def json_add():
    try:
        atfemail = ATFEmail()
        fetched_data = atfemail.email_data()
        json_data = fetched_data["json_list"]
        json_list = []
        for data in json_data:
            json_list.append(EmailJson(data[0],data[1],data[2]))
        db.session.add_all(json_list)
        db.session.commit()
        return "Created Successfully"
    except Exception as e:
        return(str(e))

@flaskpoc.route('/delete/<id_>')
def json_delete_by_id(id_):
    try:
        data = EmailJson.query.filter_by(id=id_).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            return "Deleted Successfully"
        else:
            return "No Data Found!"
    except Exception as e:
        return (str(e))


@flaskpoc.route("/getall")
def json_get_all():
    try:
        datas=EmailJson.query.all()
        if datas:
            results = return_value(datas)
            return {"count": len(results), "values": results}
        else:
            return "No Data Found!"
    except Exception as e:
        return(str(e))

@flaskpoc.route("/get/<id_>")
def json_get_by_id(id_):
    try:
        data=EmailJson.query.filter_by(id=id_).first()
        if data:
            results = return_value(data)
            return jsonify(results)
        else:
            return "No Data Found!"
    except Exception as e:
        return(str(e))

def return_value(datas):
    if isinstance(datas,list):
        results = [
            {
                "email_from": data.email_from,
                "subject": data.subject,
                "json_value": data.json_value
            } for data in datas]
        return results
    else:
        results ={
                "email_from": datas.email_from,
                "subject": datas.subject,
                "json_value": datas.json_value
            }
        return results

