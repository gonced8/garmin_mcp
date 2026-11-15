import pytest
from garmin_mcp.workouts import _normalize_workout_steps


@pytest.mark.parametrize("field,value", [
    ("targetType", {"workoutTargetTypeId": 1, "workoutTypeKey_ignore": ""}),
    ("strokeType", {"strokeTypeId": 6, "strokeTypeKey": "backstroke"}),
    ("equipmentType", {"equipmentTypeId": 1, "equipmentTypeKey": "pull_buoy"}),
    ("stepType", {"stepTypeId": 5, "stepTypeKey": "interval"}),
    ("equipmentType", {"equipmentTypeId": 2, "unknown": True}),
])
def test_bad_enum(field, value):
    with pytest.raises(ValueError):
        _normalize_workout_steps({"workoutSegments": [{"workoutSteps": [{field: value}]}]})
