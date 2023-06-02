### デプロイ方法
```
gcloud functions deploy python-http-function \          
--gen2 \
--runtime=python311 \
--region=asia-east1 \
--source=. \
--entry-point=main \
--trigger-http \
--allow-unauthenticated
```