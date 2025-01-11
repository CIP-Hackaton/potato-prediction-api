# Potato Prediction API

A REST API developed with FastAPI to predict ideal potato characteristics based on specific conditions and an AI model. This system allows farmers and researchers to obtain accurate predictions about the most suitable potato varieties for their particular conditions.

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Main Modules](#main-modules)
- [API Endpoints](#api-endpoints)
- [AI Model](#ai-model)
- [Database](#database)
- [Authentication and Authorization](#authentication-and-authorization)
- [Setup and Deployment](#setup-and-deployment)

## 🏗️ Project Structure

```
.
├── app/
│   ├── ai/                    # Artificial Intelligence Module
│   ├── api/                   # Endpoints and routes definition
│   ├── db/                    # Database configuration
│   ├── middleware/            # Application middlewares
│   ├── models/                # SQLAlchemy models
│   ├── repositories/          # Data access layer
│   ├── schemas/               # Pydantic schemas
│   ├── services/              # Business logic
│   └── utils/                 # General utilities
```

## 🛠️ Technologies Used

- **FastAPI**: Modern and fast web framework for building APIs
- **SQLAlchemy**: ORM for database interaction
- **TensorFlow**: Framework for AI model
- **JWT**: Token-based authentication
- **Dependency Injector**: Dependency management
- **Pydantic**: Data validation and configuration
- **PostgreSQL**: Relational database

## 🏛️ Architecture

The project follows a layered architecture:

1. **API Layer** (`app/api/`): Handles HTTP requests
2. **Service Layer** (`app/services/`): Implements business logic
3. **Repository Layer** (`app/repositories/`): Manages data access
4. **Data Layer** (`app/models/`): Defines database structure

## 📦 Main Modules

### AI Module (`app/ai/`)
- `model.py`: Implements potato characteristics prediction model
- Pre-trained datasets and models in `datasets/` and `models/`
- Automatic prediction capability based on environmental conditions

### API Module (`app/api/`)
Organized in versions (v1) with the following main endpoints:

#### Endpoints (`app/api/v1/endpoints/`)
- `auth.py`: User authentication and registration
- `health.py`: Service health check
- `potatoes.py`: Potato information management
- `predictions.py`: Predictions handling
- `user.py`: User management

### Models (`app/models/`)
- `potatoes.py`: Model for potato varieties
- `predictions.py`: Model for storing predictions
- `role.py`: Model for user roles
- `user.py`: Model for users

## 🔄 API Endpoints

### Authentication
```
POST /api/v1/auth/register - Register new users
POST /api/v1/auth/login    - User login
```

### Predictions
```
POST /api/v1/predict       - Make new prediction
GET  /api/v1/predictions   - Get user predictions
GET  /api/v1/predictions/{id} - Get specific prediction
PUT  /api/v1/predictions/{id} - Update prediction
```

### Potatoes
```
GET  /api/v1/potatoes      - List all varieties
GET  /api/v1/potatoes/{id} - Get specific variety
GET  /api/v1/potatoes/{id}/characteristics - Get characteristics
```

### User
```
GET  /api/v1/user/me       - Get user profile
GET  /api/v1/user/validate - Validate user token
```

## 🧠 AI Model

The system uses a trained AI model to predict ideal potato characteristics based on:

- Weather conditions
- Geographic location
- Season of the year
- Soil characteristics

### Datasets
- `DistrToVectorNormal.csv`: Normalized district data
- `TablaNumerizadaParaModelo.csv`: Numerical data for training
- `Variedad_a_Caracteristicas_28_numeric.csv`: Variety to characteristics mapping

## 🗄️ Database

The system uses PostgreSQL with the following main models:

- **Users**: Stores user information
- **Predictions**: Records made predictions
- **Potatoes**: Potato varieties catalog
- **Roles**: User roles management

## 🔐 Authentication and Authorization

- JWT implementation for authentication tokens
- Authentication middleware to protect routes
- User roles: Farmer and Researcher
- Role-based permissions management

## ⚙️ Setup and Deployment

### Required Environment Variables
```
DATABASE_URL=postgresql://user:password@localhost:5432/db
SALT_ROUNDS=10
JWT_SECRET_KEY=your-secret-key
```

### Local Installation
```bash
# Clone repository
git clone https://github.com/yourusername/potato-prediction-api.git


# create a enviroment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


# Start server
fastapi dev app/main.py
```

### Deployment

The project is configured to be easily deployable on any cloud platform thanks to its Dockerfile. It is currently deployed on Railway.

#### Railway
The project is deployed and running on Railway, which offers:
- Automatic deployment from GitHub
- Environment variables management
- Log monitoring
- Automatic scaling

#### Docker
You can also easily deploy on any platform that supports containers:

```bash
# Build image
docker build -t potato-prediction-api .

# Run container
docker run -p 8000:8000 potato-prediction-api
```

The included Dockerfile is optimized for production and can be used to deploy on:
- Railway
- Google Cloud Run
- AWS ECS
- Azure Container Instances
- Any platform that supports Docker containers

## 📝 License

This project is under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👥 Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

