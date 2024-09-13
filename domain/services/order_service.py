# actual port implementation
from domain.use_cases.order_management_use_case import OrderManagementUseCase

class OrderManagementService(OrderManagementUseCase):
    def create(self):
        raise Exception("Not implemented")
    
    def cancel(self):
        raise Exception("Not implemented")
