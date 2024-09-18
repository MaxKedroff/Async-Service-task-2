from fastapi import FastAPI, HTTPException
import httpx
import uvicorn

API_URL = "https://jsonplaceholder.typicode.com/users"
app = FastAPI()

@app.get('/user/{user_id}')
async def get_user_by_id(user_id):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f'{API_URL}/{user_id}')
            if response.status_code == 200:
                user_data = response.json()
                return_info = {
                    'name' : user_data.get('name'),
                    'email': user_data.get('email')
                }
                return return_info
            else:
                raise HTTPException(status_code=response.status_code, detail="User not found")
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=str(e))

uvicorn.run(app, host='127.0.0.1', port=9000)