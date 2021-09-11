class Config:
  def __init__(self, env):
    
    SUPPORTED_ENVS = ["dev", "qa"]
    
    env = env.lower()
    
    if env not in SUPPORTED_ENVS:
      raise Exception(f"{env} is not a supported environment. Suppored envs: {SUPPORTED_ENVS}")
    
    self.base_url = {
      "dev": "https://mydev-env.com",
      "qa": "https://myqa-env.com"
    }[env]
    
    self.app_port = {
      "dev": 8080,
      "qa": 80
    }[env]
