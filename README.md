# f1-fanProject
Here's a *30-Day Phase 1 Roadmap* with specific learning resources and actionable steps, optimized for a solo developer:

---

### 📚 *Pre-Phase Learning (Days 0-3)*
*Essential Skills to Acquire*:
1. *Basic Kafka*:  
   - [Conduktor Kafka 10-Minute Crash Course](https://www.conduktor.io/kafka/academy/kafka-10-min-tutorial)  
   - Learn: Topics, Producers, Consumers  
   - Key Concept: "Kafka is just a distributed log"

2. *Spring Boot Fundamentals*:  
   - [Spring Boot in 100 Seconds (Video)](https://youtu.be/jHcw5Fto5SU)  
   - [Official Getting Started Guide](https://spring.io/guides/gs/spring-boot/)  

3. *React Basics*:  
   - [React Official Tutorial](https://react.dev/learn) (Just "Tic-Tac-Toe" section)  

---

### 🗓 *Daily Breakdown*
#### *Days 1-3: Fake Data Pipeline*
*Goal*: Generate fake F1 telemetry  
- *Task 1*: Python script sending mock data to Kafka  
  python
  # Install: pip install kafka-python
  from kafka import KafkaProducer
  import time, random

  producer = KafkaProducer(bootstrap_servers='localhost:9092')
  drivers = ['VER', 'HAM', 'LEC']

  while True:
      driver = random.choice(drivers)
      speed = random.randint(200, 350)
      msg = f"{driver},{speed},{random.randint(8000, 12000)}"
      producer.send('f1-telemetry', msg.encode())
      time.sleep(0.5)
  
- *Resource*: [kafka-python Docs](https://kafka-python.readthedocs.io/)  

#### *Days 4-7: Local Kafka Setup*  
*Goal*: Working Kafka cluster on your machine  
- *Task*:  
  bash
  # Using Docker
  curl -sSL https://raw.githubusercontent.com/conduktor/kafka-stack-docker-compose/master/zk-single-kafka-single.yml > docker-compose.yml
  docker-compose up -d
  
- *Verify*:  
  bash
  docker exec -it kafka /bin/sh
  kafka-console-consumer --bootstrap-server localhost:9092 --topic f1-telemetry
  
- *Resource*: [Docker/Kafka Cheatsheet](https://developer.confluent.io/quickstart/kafka-docker/)

---

#### *Days 8-12: Java Backend Foundation*  
*Goal*: Consume Kafka messages in Spring Boot  
- *Task*: Create a Kafka consumer  
  java
  // pom.xml dependency: spring-kafka
  @SpringBootApplication
  public class TelemetryConsumer {
      public static void main(String[] args) {
          SpringApplication.run(TelemetryConsumer.class, args);
      }

      @KafkaListener(topics = "f1-telemetry")
      public void listen(String message) {
          String[] parts = message.split(",");
          System.out.printf("%s: %s km/h%n", parts[0], parts[1]);
      }
  }
  
- *Resource*: [Spring Kafka Guide](https://spring.io/guides/gs/messaging-kafka/)

---

#### *Days 13-16: Basic Frontend*  
*Goal*: Show speed/RPM in React  
- *Task*:  
  1. Create React app: npx create-react-app f1-dashboard  
  2. Add WebSocket connection:  
     javascript
     // App.js
     const [speed, setSpeed] = useState(0);
     useEffect(() => {
       const ws = new WebSocket('ws://localhost:8080/telemetry');
       ws.onmessage = (event) => {
         const data = JSON.parse(event.data);
         setSpeed(data.speed);
       };
     }, []);
     
  3. Simple display:  
     jsx
     <h1>{speed} km/h</h1>
     
- *Resource*: [React WebSocket Guide](https://blog.logrocket.com/websockets-tutorial-how-to-go-real-time-with-node-and-react-8e4693fbf843/)

---

#### *Days 17-20: Prediction Feature*  
*Goal*: "Guess next pit stop" system  
- *Task*:  
  1. Add Redis:  
     bash
     docker run -p 6379:6379 redis
     
  2. Store predictions:  
     java
     // Java
     @Autowired private RedisTemplate<String, String> redisTemplate;

     public void savePrediction(String user, int lap) {
         redisTemplate.opsForZSet().add("predictions", user, lap);
     }
     
  3. React form to submit guesses  
- *Resource*: [Spring Data Redis](https://spring.io/guides/gs/spring-data-redis/)

---

#### *Days 21-25: Deployment*  
*Goal*: Host MVP online  
- *Backend*:  
  bash
  # Heroku (Java)
  heroku create
  git push heroku main
  
- *Frontend*:  
  bash
  # Netlify (React)
  npm run build
  drag-and-drop build folder to Netlify
  
- *Resource*: [Heroku Java Guide](https://devcenter.heroku.com/articles/deploying-spring-boot-apps)

---

#### *Days 26-30: Add Weather API*  
*Goal*: Show track weather  
- *Task*:  
  1. Get OpenWeatherMap API key (free tier)  
  2. Feign client in Spring Boot:  
     java
     @FeignClient(name = "weather", url = "https://api.openweathermap.org")
     public interface WeatherClient {
         @GetMapping("/data/2.5/weather?lat={lat}&lon={lon}&appid={key}")
         String getWeather(@PathVariable double lat, 
                          @PathVariable double lon, 
                          @PathVariable String key);
     }
     
  3. Display on frontend  
- *Resource*: [OpenWeatherMap API Docs](https://openweathermap.org/current)

---

### 🛠 *Tool Stack for Phase 1*
| Tool           | Purpose                          | Resource                                      |
|----------------|----------------------------------|-----------------------------------------------|
| Docker Desktop | Local Kafka/Redis                | [Docker Install](https://www.docker.com/)     |
| IntelliJ IDEA  | Java Development                 | [Free Community Edition](https://www.jetbrains.com/idea/download/) |
| VS Code        | React/Python                     | [Download](https://code.visualstudio.com/)    |
| Postman        | API Testing                      | [Download](https://www.postman.com/)          |

---

### 🚨 *Troubleshooting Guide*
1. *Kafka Not Connecting*:
   - Check localhost:9092 is accessible
   - Run docker ps to confirm containers are up

2. *React WebSocket Issues*:
   - Ensure CORS is configured in Spring Boot:  
     java
     @Configuration
     public class WebConfig implements WebMvcConfigurer {
         @Override
         public void addCorsMappings(CorsRegistry registry) {
             registry.addMapping("/**").allowedOrigins("*");
         }
     }
     

3. *Heroku Deployment Failures*:
   - Use heroku logs --tail
   - Verify Procfile: web: java -jar target/*.jar

---

### 🌟 *Success Metrics for Phase 1*
- ✅ Kafka streams fake data to Java backend  
- ✅ React shows real-time speed updates  
- ✅ Users can submit pit stop predictions  
- ✅ Weather data appears on dashboard  
- ✅ App deployed and shareable via URL  

Ready to start? Pick a Day 1 task and I'll provide the exact code/config needed! 🚦
