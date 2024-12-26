import serial
import keyboard
import time

# 시리얼 포트 설정 (COM 포트는 본인 환경에 맞게 변경)
ser = serial.Serial('COM8', 9600)

while True:
    try:
        data = ser.readline().decode().strip().split(',')
        if len(data) == 3:
            x, y, button = map(int, data)
            
            # 조이스틱 처리
            if x < 400:
                keyboard.press(0x26)
            elif x > 600:
                keyboard.press(0x28)
            else:
                keyboard.release(0x26)
                keyboard.release(0x28)
                
            if y < 400:
                keyboard.press(0x29)
            elif y > 800:
                keyboard.press(0x27)
            else:
                keyboard.release(0x27)
                keyboard.release(0x29)
                
            # 버튼 처리
            if button == 0:
                keyboard.press('enter')
            else:
                keyboard.release('enter')
                
        time.sleep(0.005)
        
    except KeyboardInterrupt:
        break
    except:
        pass

ser.close()
