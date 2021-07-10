from fastapi import FastAPI

from controller.runner import get_winner
from form.lucky_draw_form import GenerateWinnerResponse

app = FastAPI()


@app.post("/generate-winner/", response_model=GenerateWinnerResponse)
async def generate_winner(activity_id: int):
    """
    抽奖
    :param activity_id:
    :return: winner user id
    """
    uid = get_winner(activity_id)
    print("winner uid is: ", uid)
    return GenerateWinnerResponse(winner_uid=uid)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
