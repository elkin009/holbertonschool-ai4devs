class InventoryEngine:
    def calculate_recommendation(self, stock, velocity, lead_time, safety_stock):
        # Mənfi satış sürətini 0 kimi qəbul edirik
        velocity = max(0, velocity)
        
        # Alqoritm: (Satış Sürəti * Tədarük Müddəti) - Mövcud Stok + Təhlükəsizlik Stoku
        needed = (velocity * lead_time) + safety_stock
        recommendation = int(needed - stock)
        
        # Əgər nəticə mənfidirsə, deməli ehtiyac yoxdur (0)
        final_qty = max(0, recommendation)
        
        # Prioritet təyini
        priority = "High" if stock < safety_stock else "Normal"
        
        return {
            "recommendation": final_qty,
            "priority": priority
        }
