class InventoryEngine:
    def calculate_recommendation(self, stock, velocity, lead_time, safety_stock):
        velocity = max(0, velocity)
        needed = (velocity * lead_time) + safety_stock
        recommendation = int(needed - stock)
        final_qty = max(0, recommendation)
        priority = "High" if stock < safety_stock else "Normal"
        return {"recommendation": final_qty, "priority": priority}
