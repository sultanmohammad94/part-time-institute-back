from flask import Flask, jsonify, request
from pprint import pprint

app = Flask(__name__)

days = [
    "sat", "sun", "mon",
    "tus", "wed", "thu", "fri"
]

instructor_1 = {
    "t_id": 1,
    "name": "instructor_1",
    "created_at": "2023-01-01T00:00:00",
    "specialization": "programming",
    "education": "master",
    "sessions":{
        "sat":[],
        "sun":[],
        "mon":[],
        "tus":[],
        "wed":[],
        "thu":[],
        "fri":[]
    }
}

instructor_2 = {
    "t_id": 2,
    "name": "instructor_2",
    "created_at": "2023-01-01T00:00:00",
    "specialization": "MBA",
    "education": "business",
    "sessions":{
        "sat":[],
        "sun":[],
        "mon":[],
        "tus":[],
        "wed":[],
        "thu":[],
        "fri":[]
    }
}

instructor_3 = {
    "t_id": 3,
    "name": "instructor_3",
    "created_at": "2023-01-01T00:00:00",
    "specialization": "Math",
    "education": "Science",
    "sessions":{
        "sat":[],
        "sun":[],
        "mon":[],
        "tus":[],
        "wed":[],
        "thu":[],
        "fri":[]
    }
}


def generate_sessions(start, end, duration):
    """Generates sessions for a given day

    Args:
        day (str): day as string
        start (float): starting hour using 24 hour clock format
        end (float): ending hour using 24 hour clock format
        duration (float): a float value representing the duration for each session 0.5 is half hour, 2 is two hours and so on
        
    Returns:
        dict: available sessions for a given day and session duration.
    """
    avaliable_sessions = []
    while session_end:= start < end:
        session_end = start + duration
        avaliable_sessions.append(
            {"start": start, "end": session_end, "is_booked": False , "std_id": None}
        )
        start = session_end
        
    return avaliable_sessions

def get_shift(shift_days: list, start: float, end: float, duration: float)->dict:
    avaliable_sessions = {}
    for sd in shift_days:
        day_sessions = generate_sessions(start, end, duration)
        avaliable_sessions.update({sd: day_sessions})
    return avaliable_sessions

def generate_instructor_one_sessions():
    shift_days = [d for d in days if d != "fri"]
    start, end = 11, (9 + 12)
    duration = 2
    return get_shift(shift_days, start, end, duration)

def generate_instructor_two_sessions():
    shift_days = [d for d in days if d != "fri"]
    start, end = (4+12), (9 + 12)
    duration = 2
    return get_shift(shift_days, start, end, duration)
    
def generate_instructor_three_sessions():
    avaliable_sessions = {}
    shift_1 = ["mon", "tus", "wed"]
    shift_2 = ["sat"]
    start_1, end_1 = (5+12), (11 + 12)
    start_2, end_2 = (10), (10 + 12)
    duration = 2
    r1 = get_shift(shift_1, start_1, end_1, duration )
    r2 = get_shift(shift_2, start_2, end_2, duration )
    r2.update(r1)
    return r2
    
instructors = [
    instructor_1,
    instructor_2,
    instructor_3
]

@app.route('/v1/avaliable_sessions/')
def get_instructors_sessions():
    inst1_sessions = generate_instructor_one_sessions()
    instructors[0]['sessions'] = inst1_sessions
    inst2_sessions = generate_instructor_two_sessions()
    instructors[1]['sessions'] = inst2_sessions
    inst3_sessions = generate_instructor_three_sessions()
    instructors[2]['sessions'] = inst3_sessions
    data = instructors
    return jsonify({"data": data})

@app.route('/v1/avaliable_sessions/<int:id>')
def get_instructor_sessions(id: int):
    
    is_inst_exist = False if (id-1) >= len(instructors) or not instructors[id-1] else True
    if not is_inst_exist:
        return "Instructor does not exist"
    if instructors[0]['t_id'] == id:
        inst1_sessions = generate_instructor_one_sessions()
        instructors[0]['sessions'] = inst1_sessions
        return jsonify({"data": instructors[0]})
    elif  instructors[1]['t_id'] == id:
        inst2_sessions = generate_instructor_two_sessions()
        instructors[1]['sessions'] = inst2_sessions
        return jsonify({"data": instructors[1]})
    else:
        inst3_sessions = generate_instructor_three_sessions()
        instructors[2]['sessions'] = inst3_sessions
        return jsonify({"data": instructors[2]})

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    print(f'>>Running on Machine {HOST}:{PORT} with debug mode {"Enabled" if DEBUG else "Disabled"}')
    app.run(HOST, PORT, debug=DEBUG)