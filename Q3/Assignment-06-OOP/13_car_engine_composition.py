class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        return f"{self.engine_type} engine started"

    def get_specs(self):
        return f"Engine type: {self.engine_type}"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Car has-an Engine
    
    def start_engine(self):
        return f"{self.model}: {self.engine.start()}"
    
    def get_full_specs(self):
        return f"{self.model} with {self.engine.get_specs()}"

# Create an Engine
v8_engine = Engine("V8")

# Create a Car with the Engine (composition)
mustang = Car("Ford Mustang", v8_engine)

# Access Engine methods through Car
print(mustang.start_engine())      
print(mustang.get_full_specs())     