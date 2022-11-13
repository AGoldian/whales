# **Indentification of bowhead whales**

Реализовано веб-приложения для индетификации гренландских китов. Для отслеживания миграции и популяции семейства.

### **Установка и запуск**

Clone the repo and change to the project root directory:
```
git clone https://github.com/AGoldian/whales.git
cd whales
```

Install requirements:
```
pip install -r requirements.txt
```

And run:
```
streamlit run streamplit_app.py
```

### **Пример работы**

![demo](https://github.com/AGoldian/whales/blob/main/resources/whales_demo.gif?raw=true)

## **Используемое решение**

Технологии для решения отбирались по двум критериям - это автономность работы решения и наличие библиотек открытого доступа. 
После чего мы провели сравнительный анализ, выбрав модели оптимальные по соотношению точности к требуемой производительности - ResNet101, VGG19 и EfficientNet.