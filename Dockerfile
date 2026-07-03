# --------------------------------------------------------------------------
# Bu Dockerfile, code/image security tarama araçlarını (SCA, IaC, admission
# control, runtime security vb.) test etmek amacıyla hazırlanmıştır.
# Kasıtlı olarak barındırdığı bazı yaygın "finding"ler aşağıda not edilmiştir.
# Production'da KULLANMAYIN.
# --------------------------------------------------------------------------

# [Finding] Sabit/eski bir base image tag'i - "latest" veya major-only tag
FROM python:3.9

# [Finding] Gereksiz paketler ve apt cache temizlenmiyor (image boyutu + CVE yüzeyi)
RUN apt-get update && apt-get install -y curl vim netcat

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# [Finding] Ortam değişkeni içine hardcoded "secret" (test amaçlı, gerçek değer değil)
ENV API_KEY="sample-hardcoded-api-key-12345"

# [Finding] Container root kullanıcı ile çalışıyor (USER direktifi yok)
# [Finding] Genişletilmiş/gereksiz port aralığı yerine tek port yeterliyken:
EXPOSE 8080

# [Finding] HEALTHCHECK tanımlı değil

CMD ["python", "app.py"]
