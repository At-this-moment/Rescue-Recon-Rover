# Rescue-Recon-Rover (3R)

**재난현장 정보수집 로봇** — 원격에서 요구조자의 위치와 현장 환경 정보를 수집하는 궤도형 로봇

---

![92](https://github.com/user-attachments/assets/805f98ef-2663-40db-a9d7-30530537c360)

| ![Screenshot (6)](https://github.com/user-attachments/assets/4a0322e2-bc5c-45dc-a664-f29611dba0b8) | ![IMG_1274](https://github.com/user-attachments/assets/8a42778c-794e-4842-9ee6-6ce39ca56178) | ![IMG_1287](https://github.com/user-attachments/assets/7ad7d31f-0058-4998-839e-e3f0ed4046b9) |
|:---:|:---:|:---:|
| 장착된 적외선 카메라 테스트 | 라즈베리파이 나노 | ...... |
| ![IMG_1329](https://github.com/user-attachments/assets/bbc7b33a-6e29-4d62-9456-5c23dbd5246e) | ![IMG_1331](https://github.com/user-attachments/assets/341e881d-41ed-4db8-bede-861ea5a4c75d) | ![IMG_1337](https://github.com/user-attachments/assets/c30b978b-be64-4db5-a437-e7a12e070790) |
| 작동정지의 원인이었던 접촉 불량 | 모터컨트롤러를 기울여 장착하여 해결 | 완성된 Rescue-Recon-Rover 전면 모습 |


---

## 프로젝트 개요

**Rescue-Recon-Rover(3R)** 는 재난 현장에서 투입되어 **원격 조종**, **실시간 영상 전송**, **환경 정보 수집**을 수행하는 라즈베리파이 기반 궤도 로봇입니다.
장애물 지형을 주행하며 요구조자 위치 파악과 주변 상황 분석을 지원합니다.

---

## 주요 사양

| 구분         | 사양                                           |
| ---------- | -------------------------------------------- |
| **컨트롤러**   | Raspberry Pi Zero WH                         |
| **주행 제어기** | Microsoft Xbox Controller QAS-00001 (USB/BT) |
| **구동 모터**  | Micro DC metal geared motor × 2              |
| **영상 장치**  | PiCamera (실시간 MJPEG 스트리밍)                    |
| **환경 센서**  | DHT11 (온·습도), AMG8833 (열화상, 추후 확장)           |
| **전원**     | Eneloop AA 배터리 팩                             |
| **구동 방식**  | 좌/우 트랙 기반 차동 구동                              |
| **프레임/차체** | 소형 궤도형 섀시, 경량 구조                             |

---

## 코드 구성

```
.
├─ camera.py        # PiCamera MJPEG 스트리밍 서버(:8000)
├─ final.py         # pygame 기반 주행/속도 제어
├─ main.py          # curses 기반 주행 제어 + 부저 테스트
├─ sensor2.py       # DHT11 온·습도 센서 측정
├─ sensor.py        # 디지털 입력 상태 출력
├─ key-test.py      # curses 키 입력 테스트
└─ key-test-2.py    # pygame 키 입력 테스트
```

---

## ⚙설치 및 실행

### 1. 의존성 설치

```bash
sudo apt update
sudo apt install -y python3-pip python3-picamera python3-pygame
pip3 install RPi.GPIO Adafruit_DHT
```

### 2. 카메라 스트리밍 서버

```bash
python3 camera.py
# 브라우저에서 http://<라즈베리파이_IP>:8000 접속
```

### 3. 주행 제어

* **pygame 기반 (`final.py`)**

```bash
python3 final.py
# ↑↓←→ : 전후좌우 / 1,2,3 : 속도 변경 / q : 종료 / s : 셧다운
```

* **curses 기반 (`main.py`)**

```bash
python3 main.py
# ↑↓←→ : 전후좌우 / Enter : 정지 / q : 종료 / S : 셧다운
```

### 4. 센서 테스트

```bash
python3 sensor2.py   # DHT11 온·습도
python3 sensor.py    # 디지털 입력 상태
```

---

## 기능 요약

* **실시간 영상**: PiCamera로 MJPEG 스트리밍
* **원격 주행**: 키보드/게임패드로 방향 및 속도 제어
* **환경 측정**: 온·습도 / 추후 열화상 센서 통합 가능
* **간단 구조**: 모듈형 코드로 각 기능 독립 실행 가능
