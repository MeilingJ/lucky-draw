from fastapi import APIRouter

from controller.runner import get_winner
from form.lucky_draw_form import GenerateWinnerResponse

router = APIRouter()


@router.post("/generate-winner/", response_model=GenerateWinnerResponse)
async def generate_winner(activity_id: int):
    """
    抽奖
    :param activity_id:
    :return: winner user id
    """
    uid = get_winner(activity_id)
    print("winner uid is: ", uid)
    return GenerateWinnerResponse(winner_uid=uid)



