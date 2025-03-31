#!/usr/bin/env python3

import serial
import LED_pb2
import random
import time

def send_led_command(ser, value,quiet=0):
    request = LED_pb2.LedControl()
    request.LED = value
    data = request.SerializeToString()
    ser.write(data)
    
    if (not quiet):
        led_status = LED_pb2.LedControl()
        led_status.ParseFromString(data)
        print(f"Sent: {led_status}")

def stress_test(ser, duration=10):
    print(f"Starting stress test for {duration} seconds...")
    start_time = time.time()
    while time.time() - start_time < duration:
        send_led_command(ser, random.randint(0, 1), quiet = 1)
    print("\nStress test complete.")

def send_arbitrary_bytes(ser, byte_data):
    try:
        if isinstance(byte_data, str):  # Allow string input
            byte_data = bytes.fromhex(byte_data.replace(" ", ""))  # Convert hex string to bytes
        elif isinstance(byte_data, list):  # Allow list of integers
            byte_data = bytes(byte_data)
        
        ser.write(byte_data)
        print(f"Sent raw bytes: {byte_data.hex()}")
    except:
        print("\nError sending arbitrary bytes.")


def main():
    try:
        ser = serial.Serial("COM" + input("Enter COM number: "), 115200)
    except:
        print(f"Error connecting.")
    else:
        print(f"Connected to {ser.name}")
    
        while True:
            print("Select mode: \n1. Manual Mode \n2. Stress Test Mode \n3. Send Raw Bytes \n4. Exit")
            mode = input("Enter choice: ")
            
            if mode == '1':
                while True:
                    value = input("Turn LED on/off (1/0, or 'b' to go back): ")
                    if value == 'b':
                        break
                    elif value in ('0', '1'):
                        send_led_command(ser, int(value))
                    else:
                        print("Invalid input. Enter 1, 0, or 'b' to go back.")
            
            elif mode == '2':
                duration = input("Enter stress test duration in seconds (default 10): ")
                duration = int(duration) if duration.isdigit() else 10
                stress_test(ser, duration)
            
            elif mode == '3':
                raw_data = input("Enter raw bytes (hex format, e.g., 'FF 01 02'): ")
                send_arbitrary_bytes(ser, raw_data)
            
            elif mode == '4':
                print("Exiting...")
                ser.close()
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
