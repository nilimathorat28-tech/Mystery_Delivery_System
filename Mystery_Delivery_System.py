import json
import math


#---------------------------------------------------------------
# Calculate Euclidean distance between two coordinate points
# Formula: sqrt((x2-x1)^2 + (y2-y1)^2)
#---------------------------------------------------------------
def calculate_distance(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

#---------------------------------------------------------------

# Find the nearest delivery agent to a given warehouse location
# Tie-breaking rule:If distances are equal, choose lexicographically
# smaller agent ID(e.g., A1 < A2)
#----------------------------------------------------------------

    
def find_nearest_agent(warehouse_location,agents):
    min_distance = float('inf')
    nearest_agent = None
    
    for agent_id, agent_data in agents.items():
        dist = calculate_distance(agent_data["location"],warehouse_location)
        if dist < min_distance or (dist == min_distance and (nearest_agent is None or agent_id < nearest_agent)):
            min_distance = dist
            nearest_agent = agent_id
    return nearest_agent, min_distance

#--------------------------------------------------------------
#Simulate package deliveries:
#1. Normalize JSON structures (agents & warehouses)
#2. Assign each package to nearest agent
#3. Compute total distance traveled
#4. Generate performance report
#---------------------------------------------------------------

def simulate_delivery(data):
    
    packages = data["packages"]

    # Normalize agents structure(supports both list and dict JSON formats)
    raw_agents = data["agents"]

    #Convert agents into uniform dict:{"A1":{"location":[x,y]}}

    if isinstance(raw_agents,list):
        agents = {a["id"]: {"location":a["location"]} for a in raw_agents}
    else:
        agents = {k: {"location":v} for k,v in raw_agents.items()}

    #Normalize warehouse structure(supports both list and dict JSON formats)
    raw_warehouse = data["warehouses"]

    #Convert warehouses into uniform dict:{"W1":{"location":[x,y]}}
    if isinstance(raw_warehouse,list):
        warehouse = {w["id"]: {"location":w["location"]} for w in raw_warehouse}
    else:
        warehouse = {k: {"location":v} for k,v in raw_warehouse.items()}
    
    # Initialize report structure for each agent
    report = {}
    for agent_id in agents:
        report[agent_id] = {"packages_delivered":0,"total_distance":0}

    # Process each package
    for package in packages:

        #Safe warehouse id extraction (supports ALL test cases)
        if "warehouse_id" in package:
            wh_id = package["warehouse_id"]

            #base_case.json
        elif "warehouse" in package:
            wh_id = package["warehouse"]

            #test_case_1 to test_case_10
        else:
            raise KeyError("Warehouse reference missing in package")

        warehouse_data = warehouse[wh_id]
        destination = package["destination"]

        #Find nearest agent to warehouse
        agent_id, dist_to_warehouse = find_nearest_agent(warehouse_data["location"],agents)

        #Distance from warehouse to customer destination 
        dist_wh_to_dest = calculate_distance(warehouse_data["location"],destination)

        #Total distance for this delivery trip
        total_trip = dist_to_warehouse + dist_wh_to_dest

        #Update agent performance report
        report[agent_id]["packages_delivered"] += 1
        report[agent_id]["total_distance"] +=total_trip

    #Calculate efficiency for each agent
    for agent in report:
        delivered = report[agent]["packages_delivered"]
        if delivered > 0:
            report[agent]["efficiency"] = round(report[agent]["total_distance"]/delivered,2)
        else:
            report[agent]["efficiency"] = 0
        report[agent]["total_distance"] = round(report[agent]["total_distance"],2)
    return report

#--------------------------------------------------------------------------------------
# Identify the most efficient agent based on minimum
# Average distance per delivery
#---------------------------------------------------------------------------------------

    
def find_most_efficient(report):
    return min(report, key = lambda x:report[x]["efficiency"] if report[x]["efficiency"] > 0 else float('inf'))

#----------------------------------------------------------------------------------------
# Main execution block
#----------------------------------------------------------------------------------------
if __name__ == "__main__":
    

    #Run and parse JSON test input file
    file_path = "test_cases/base_case.json"

    with open(file_path,"r") as f:
        data = json.load(f)

    #Run simulation
    report = simulate_delivery(data)

    #Identify best performing agent
    best_agent = find_most_efficient(report)
    report["best_agent"] = best_agent

    #Print formatted delivery report
    print("\nDelivery Report:\n")
    print(json.dumps(report, indent=4))

    #Save final report to JSON file
    with open("report.json", "w") as f:
        json.dump(report,f,indent = 4)
