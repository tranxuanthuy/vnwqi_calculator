from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import io
from utils.wqi4df import calculate_wqi_for_df

app = FastAPI()

@app.post("/calculate_vnwqi_csv")
async def calculate_vnwqi_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Chỉ chấp nhận file CSV")
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))

        # Gọi hàm tính toán WQI cho DataFrame
        df_result = calculate_wqi_for_df(df)

        output = io.StringIO()
        df_result.to_csv(output, index=False, encoding='utf-8')
        content = output.getvalue()

        headers = {
            "Content-Disposition": "attachment; filename=wqi_results.csv"
        }

        async def generate():
            yield content.encode('utf-8')

        return StreamingResponse(generate(), media_type="text/csv", headers=headers)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi xử lý file CSV: {str(e)}")