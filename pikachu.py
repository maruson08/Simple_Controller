import serial
import keyboard
import time

# 시리얼 포트 설정 (COM 포트는 본인 환경에 맞게 변경)
ser = serial.Serial('COM7', 9600)

while True:
    try:
        data = ser.readline().decode().strip().split(',')
        if len(data) == 3:
            x, y, button = map(int, data)
            
            # 조이스틱 처리
            if x < 400:
                keyboard.press('d')
            elif x > 600:
                keyboard.press('g')
            else:
                keyboard.release('d')
                keyboard.release('g')
                
            if y < 400:
                keyboard.press('f')
            elif y > 800:
                keyboard.press('r')
            else:
                keyboard.release('r')
                keyboard.release('f')
                
            # 버튼 처리
            if button == 0:
                keyboard.press('x')
            else:
                keyboard.release('x')
                
        time.sleep(0.005)
        
    except KeyboardInterrupt:
        break
    except:
        pass

ser.close()
