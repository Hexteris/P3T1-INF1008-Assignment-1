import math
import random
import time

NUM_UNIQUE_CARS = 6700  # Number of registered cars in the traffic flow
REPEAT_SCANS = 100       # Additional repeat scans to simulate sensor jitter/congestion
UNREGISTERED_IDS = [99, 88, 21, 25] # Unregistered IDs to test security logic

def check_lta_registry(vehicle_ids, target_id):
    """
    O(lg n) Task: Binary search in the LTA Vehicle Registry.
    Assumption: vehicle_ids is a pre-sorted, unique list of registered cars.
    """
    low = 0
    high = len(vehicle_ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if vehicle_ids[mid] == target_id:
            return True
        elif vehicle_ids[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return False

def process_erp_billing(vehicle_list, low, high, registry, stats=None):
    """
    Main Recurrence: T(n) = 3T(n/2) + lg n
    Implements recursive 'Merging Zone' verification for high accuracy.
    """
    if stats is None:
        stats = {"total_collected": 0.0, "fines_issued": 0.0, "verified_vehicles": {}}

    n = high - low
    
    # Base Case: Individual vehicle scan
    if n == 1:
        v_id = vehicle_list[low]
        is_valid = check_lta_registry(registry, v_id)
        
        # Track how many times this specific ID was scanned
        stats["verified_vehicles"][v_id] = stats["verified_vehicles"].get(v_id, 0) + 1
        
        # Only charge the first time an ID is processed
        if stats["verified_vehicles"][v_id] == 1:
            if is_valid:
                stats["total_collected"] += 2.00
            else:
                stats["fines_issued"] += 70.00
        return stats

    if n < 1:
        return stats

    # Log n work representing the LTA registry lookup
    check_lta_registry(registry, vehicle_list[low])

    # 3T(n/2) Recursive calls representing Expressway, Arterial, and Merging Zones
    mid_point = low + (n // 2)
    quarter_offset = n // 4
    
    # 1. Left Sub-zone (Arterial Logic)
    process_erp_billing(vehicle_list, low, mid_point, registry, stats)
    
    # 2. Right Sub-zone (Expressway Logic)
    process_erp_billing(vehicle_list, mid_point, high, registry, stats)
    
    # 3. Merging Zone (Central Overlap Logic - the '3rd' recursive call)
    m_low = max(low, mid_point - quarter_offset)
    m_high = min(high, mid_point + quarter_offset)
    if m_high > m_low:
        process_erp_billing(vehicle_list, m_low, m_high, registry, stats)
    
    return stats

# Test Execution
if __name__ == "__main__":
    # Setup Pre-Sorted Registry (Assumption: Clean Database for O(lg n) efficiency)
    lta_registry = list(range(1000, 20000)) # 19k registered cars
    traffic_data = random.sample(lta_registry, NUM_UNIQUE_CARS)
    
    # Add repeat scans (sensor jitter) and Manual Intruders
    repeats = random.choices(traffic_data, k=REPEAT_SCANS)
    traffic_data.extend(repeats)
    traffic_data.extend(UNREGISTERED_IDS)
    random.shuffle(traffic_data)

    print(f"***ERP 2.0 Gantryless Verification Simulation***")
    print(f"Unique Registered Cars: {NUM_UNIQUE_CARS}")
    print(f"Total Raw Scans (Including repeats/intruders): {len(traffic_data)}\n")

    start_time = time.time()
    final_stats = process_erp_billing(traffic_data, 0, len(traffic_data), lta_registry)
    end_time = time.time()

    # --- Financial & Performance Analysis ---
    processing_ms = (end_time - start_time) * 1000
    total_checks = sum(final_stats['verified_vehicles'].values())
    unique_ids_processed = len(final_stats['verified_vehicles'])
    reliability_factor = total_checks / unique_ids_processed

    print(f"Processing Speed: {processing_ms:.4f} ms")
    print(f"Total Revenue:    ${final_stats['total_collected']:.2f} (Expected: ${NUM_UNIQUE_CARS * 2:.2f})")
    print(f"Total Fines:      ${final_stats['fines_issued']:.2f} (Expected: ${len(UNREGISTERED_IDS) * 70:.2f})")
    print(f"System Reliability Factor: {reliability_factor:.2f}x checks per vehicle")
    
    # Print detailed verification counts for the first 5 vehicles
    print("\nSample Verification Logs (First 5 unique IDs):")
    sample_ids = list(final_stats['verified_vehicles'].keys())[:5]
    for v_id in sample_ids:
        count = final_stats['verified_vehicles'][v_id]
        print(f"  Vehicle {v_id}: Verified {count} times")