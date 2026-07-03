# Sample Container App — Security Scanning Test Repo

Bu repo, container/code security tarama araçlarını (SCA, IaC misconfig,
admission control, runtime security vb.) test etmek amacıyla hazırlanmış
minimal bir Flask uygulamasıdır.

## İçerik

- `app.py` — Basit Flask uygulaması (`/` ve `/healthz` endpoint'leri)
- `requirements.txt` — Python bağımlılıkları
- `Dockerfile` — Kasıtlı olarak birkaç yaygın güvenlik bulgusu içerir (yorum
  satırlarında `[Finding]` olarak işaretlenmiştir):
  - Eski/major-only base image tag'i (`python:3.9`)
  - Gereksiz paket kurulumu + temizlenmeyen apt cache
  - `ENV` içine hardcoded (sahte) secret
  - Root kullanıcı ile çalışan container (USER yok)
  - Eksik `HEALTHCHECK`
- `Dockerfile.hardened` — Aynı uygulamanın, bu bulguların düzeltildiği
  güvenli versiyonu (before/after karşılaştırması için).

## Build & Run

```bash
# Kasıtlı bulgular içeren versiyon
docker build -t sample-container-app:vuln -f Dockerfile .
docker run -p 8080:8080 sample-container-app:vuln

# Hardened versiyon
docker build -t sample-container-app:hardened -f Dockerfile.hardened .
docker run -p 8080:8080 sample-container-app:hardened
```

## Not

Bu proje sadece güvenlik tarama araçlarını test etmek amacıyla hazırlanmıştır.
İçindeki "secret" değeri sahtedir, gerçek bir kimlik bilgisi değildir.
Production ortamında `Dockerfile` (vuln) dosyasını kullanmayın.
