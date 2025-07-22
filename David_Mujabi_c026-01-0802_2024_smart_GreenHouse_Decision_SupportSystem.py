import random
import time

"""The simulation sensor receiving the random inputs on the time intervals """
def simulate_sensor_decision():
    print("\n--- Welcome to The Green House Desion and Support System ---\n")
    print("\n- Advanced by Mujabi David -")

    #the initial system status
    irrigation_status = "OFF"
    shading_status = "OFF"
    print("\\n-- System watering and shading states")
    print(f"The irrigation status is: {irrigation_status}")
    print(f"The light shading status is: {shading_status}\n")

    #real time environmental input over 10 intervals from the sensor-> in my case lets implement using random values as values from the sensor
    for time_interval in range(1, 11):
        print(f"The time is: {time_interval} hour\n")

        current_humidity = random.uniform(40, 75) # in percent
        current_soil_moisture = random.uniform(35, 50) # in percent
        current_temperature = random.uniform(25, 35) #degrees
        current_light_intensity = random.uniform(0, 1000)#in lux

        #display our current values of the received inputs
        print("-- Sensor Readings received\n")
        print(f"Humidity: {current_humidity:.2f} %\n")
        print(f"Temperature: {current_temperature:.2f} (degrees celcius)\n")
        print(f"Light intensity: {current_light_intensity:.2f} lux\n")
        print(f"Soil moisture: {current_soil_moisture:.2f} %\n")
        # watering control
        if(current_soil_moisture < 30 and (current_humidity < 40 or current_temperature > 30)):
            irrigation_status = "ON"
        elif(( 35<current_soil_moisture <= 50) and current_temperature > 35):
            irrigation_status = "Light Watering"
        elif(current_soil_moisture > 70):
            irrigation_status = "Skip Watering"
        
        
        #shading control using match case
        #categorize light intensity
        if current_light_intensity < 300 :
            light_category = "VERY LOW"
        elif 300 < current_light_intensity <= 800 :
            light_category = "LOW"
        elif 800 < current_light_intensity <= 1000:
            light_category = "HIGH"
        else:
            light_category = "VERY HIGH"

        #match the light category to the cases
        match light_category:
            case "VERY LOW":
                shading_status = "Open Shades" #very low light intensity
            case "LOW":
                shading_status = "No action"
            case "HIGH":
                shading_status = "Close Partially"
            case "VERY HIGH":
                shading_status = "Close Fully" # shade is closed fully

        print("-- Message and Action to take")
        print(f"The irrigation status: {irrigation_status}")
        print(f"The Light shading status: {shading_status}")

        time.sleep(0.5)
if __name__ == "__main__":
    simulate_sensor_decision()