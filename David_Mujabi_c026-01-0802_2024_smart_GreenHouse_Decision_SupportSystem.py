import random
import time
from datetime import datetime, timedelta

# lists to store historical data for the mock AI dashboard
soil_moisture_history = []
action_log = []

#trend identification
def get_moving_average(data_list, window_size):
    if len(data_list) < window_size:
        return None # Not enough data for the moving average
    
    # average of the last window
    return sum(data_list[-window_size:]) / window_size

""" Connect the system to a mock AI dashboard that logs actions and recommends future 
watering intervals based on trends (simulate using moving average of soil moisture).
"""

def mock_ai_dashboard_recommendation(current_hour, soil_moisture_history, action_log):

    print("\n--- Mock AI Dashboard Insights ---")

    # Logged Actions for the current hour
    print(f"Logged Actions for Hour {current_hour}:")
    if action_log:
        #  latest action logged
        latest_action = action_log[-1]
        print(f"  - Irrigation: {latest_action['irrigation']}")
        print(f"  - Shading: {latest_action['shading']}")
    else:
        print("  - No actions logged yet.")

    # Watering Recommendation based on Soil Moisture Trend
    window_size = 1
    avg_soil_moisture = get_moving_average(soil_moisture_history, window_size)

    print("\nWatering Recommendation (based on 1-hour soil moisture trend):")
    if avg_soil_moisture is None:
        print("  - Not enough historical data for a trend analysis. Continue monitoring.")
    else:
        print(f"  - Last {window_size}-hour average soil moisture: {avg_soil_moisture:.2f}%")
        if avg_soil_moisture < 35:
            print("  - Recommendation: Soil moisture consistently LOW. Consider INCREASING watering frequency or duration.")
        elif 35 <= avg_soil_moisture <= 60:
            print("  - Recommendation: Soil moisture within OPTIMAL range. Maintain current watering schedule.")
        else: # avg_soil_moisture > 60
            print("  - Recommendation: Soil moisture consistently HIGH. Consider REDUCING watering frequency or duration, or check drainage.")

#main function
"""The simulation sensor receiving the random inputs on the time intervals """
def simulate_sensor_decision():
    print("\n--- Welcome to The Green House Desion and Support System ---\n")
    print("\n- Advanced by Mujabi David -")

    #the initial system status
    irrigation_status = "OFF"
    shading_status = "OFF"
    print("\n-- System watering and shading states")
    print(f"The irrigation status is: {irrigation_status}")
    print(f"The light shading status is: {shading_status}\n")

    #real time environmental input over 10 intervals from the sensor-> in my case lets implement using random values as values from the sensor
    for time_interval in range(1, 11):
        print(f"The time is: {time_interval} hour\n")

        current_humidity = random.uniform(40, 75) # in percent
        current_soil_moisture = random.uniform(20, 80) # in percent
        current_temperature = random.uniform(28, 40) #degrees
        current_light_intensity = random.uniform(0, 1500)#in lux
        current_co2_level = random.uniform(1000, 1500) #in ppm

        #display our current values of the received inputs
        print("-- Sensor Readings received")
        print(f"Humidity: {current_humidity:.2f} %")
        print(f"Temperature: {current_temperature:.2f} (degrees celcius)")
        print(f"Light intensity: {current_light_intensity:.2f} lux")
        print(f"Soil moisture: {current_soil_moisture:.2f} %")
        print(f"CO2 level: {current_co2_level:.2f} ppm\n")
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
        print(f"The Light shading status: {shading_status}\n")


        #raise alerts from the output of the sensor
        alerts = []
        alert_count = 0

        if current_temperature > 30:
            alert_count+=1;
            alerts.append("Temperature > 30");
        if current_humidity < 25 :
            alert_count +=1
            alerts.append("Humidity < 25%")
        if current_co2_level > 1200:
            alert_count+=1
            alerts.append("C02 level > 1200 ppm")
        if current_soil_moisture < 30:
            alert_count +=1
            alerts.append("Soil Moisture < 30%")
        if alert_count >=3:
            print(f"The system is in critical condition!!!\nAmong the conditions met in the system is:\n")
            for alert in alerts:
                print(f"-- {alert}")
            # return True
        else:
            print("The system is not in critical condition based on the conditions for a critical system...")

        #log the system output to a mock dashboard
        soil_moisture_history.append(current_soil_moisture)
        action_log.append({
            'hour': time_interval,
            'irrigation': 'ON' if irrigation_status else 'OFF',
            'shading': f"{shading_status}% Open",
        })
        print(f"------------------- END OF {time_interval} HOUR --------------------\n") 
        time.sleep(0.5)

    # AI dashboard
    print("\n--- End of Simulation Summary from Mock AI Dashboard ---")
    mock_ai_dashboard_recommendation(time_interval, soil_moisture_history, action_log)
    print("=== Lets Make Good Farming Techniques with advanced ai using Smart Green House Support System ===\n")

"""
#raise alerts logic
alert_count = 0
alerts=[]
***state the conditions required
while incrementing the alert counting
check if the conditions appended to the alert counts are met and are >= 3
raise an alert and print the conditions
"""

if __name__ == "__main__":
    simulate_sensor_decision()