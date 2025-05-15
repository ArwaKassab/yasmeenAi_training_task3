
# 📌 Project Overview

This project is a **Django REST API** for managing user-specific ToDo tasks. It provides API endpoints with two different execution approaches:

- **Synchronous Execution**
- **Asynchronous + Parallel Execution**

In this project, I applied the **Scatter-Gather Pattern** concept with **Asynchronous Execution** and **Parallelism** to efficiently handle multiple I/O-bound database queries concurrently without blocking the server.

---

## 💡 Concept Implemented: Scatter-Gather Pattern

In the `TaskAsyncParallelView` endpoint, I applied the **Scatter-Gather Pattern** by:

- **Scatter:** Launching multiple database queries asynchronously so they all run concurrently.
- **Gather:** Using `asyncio.gather()` to wait for all results and collect them once they're done.

This approach improves performance when dealing with multiple I/O-bound operations without overloading the server with unnecessary threads.


## 📝 Steps to Run the Project

### Step 1: Run the Backend Server (Django API)

1. Open a terminal window.
2. Navigate to the `todo_project` directory (where `manage.py` is located).
3. Run the following command to start the server:

   ```bash
   python manage.py runserver
   ```

---

### Step 2: Test the API
#### protected APIs that require a valid JWT token to access:

   * **Registering users**
   * **Logging in**
   * **protected API (CRUD FOR TASKS)** after obtaining the token.
   * **Scatter-Gather APIs**
     
#### Test Using Postman

You can test the APIs in two ways:

🔸 **Option 1:**  
Download the provided **Postman Collection** from the task submission link.

- In Postman, go to **File > Import**.
- Select the Postman collection file.
- Use the imported collection to test all API endpoints.

🔸 **Option 2:**  
Manually copy the following URLs from the project urls.py files and test them via Postman after obtaining your login token.

---

### ✅ Task APIs (Protected with Token)

| API Name                                | URL                                               | Method | Description                                                        |
|:---------------------------------------|:--------------------------------------------------|:--------|:---------------------------------------------------------------------|
| **Synchronous Task API**               | `127.0.0.1:8000/api/tasks/no-scatter-gather/`     | `GET`   | Retrieve tasks and stats sequentially                              |
| **Scatter-Gather Task API**            | `127.0.0.1:8000/api/tasks/scatter-gather/`        | `GET`   | Use Scatter-Gather (Async + Parallelism) to retrieve tasks concurrently |

**Note:**  
Both Task APIs are protected and require passing a valid JWT token in the request headers.

**Note:**  
You can test the **Scatter-Gather API** endpoint via Postman just like any other API, either using the provided collection or the URLs listed above.

---

## ⚙️ Technologies Used

- Python 3.12
- Django 5
- Django REST Framework
- PostgreSQL
- ASGI (for asynchronous support)
- asyncio, asgiref

---


# 📌 نظرة عامة على المشروع

هذا المشروع هو **Django REST API** لإدارة مهام ToDo الخاصة بكل مستخدم. يوفر نقاط نهاية API بطريقتين مختلفتين لتنفيذ العمليات:

- **تنفيذ متزامن**
- **تنفيذ غير متزامن + متوازي**

في هذا المشروع، طبقت مفهوم **نمط Scatter-Gather** مع **التنفيذ غير المتزامن** و**التوازي** لمعالجة عدة استعلامات قاعدة بيانات I/O-bound بشكل متزامن بدون حجب الخادم.

---

## 💡 المفهوم المستخدم: نمط Scatter-Gather

في نقطة النهاية `TaskAsyncParallelView`، طبقت نمط **Scatter-Gather** عن طريق:

- **التوزيع (Scatter):** إطلاق عدة استعلامات قاعدة بيانات بشكل غير متزامن بحيث تعمل كلها بالتوازي.
- **الجمع (Gather):** استخدام `asyncio.gather()` للانتظار حتى تنتهي جميع النتائج وجمعها.

هذا النهج يحسن الأداء عند التعامل مع عدة عمليات I/O-bound بدون تحميل زائد على الخادم بخيوط معالجة غير ضرورية.

---

## 📝 خطوات تشغيل المشروع

### الخطوة 1: تشغيل الخادم الخلفي (Django API)

1. افتح نافذة طرفية (Terminal).
2. انتقل إلى مجلد `todo_project` (حيث يوجد ملف `manage.py`).
3. شغّل الأمر التالي لتشغيل الخادم:

   ```bash
   python manage.py runserver
   ```

---

### الخطوة 2: اختبار  واجهات برمجة التطبيقات (APIs)  :
#### واجهات برمجة التطبيقات (APIs) المحمية التي تتطلب توكن JWT صالح للوصول:

   * **تسجيل المستخدمين**
   * **تسجيل الدخول**
   * **واجهات محمية (CRUD للمهام)** بعد الحصول على التوكن.
   * **واجهات Scatter-Gather**
     
#### الاختبار باستخدام Postman

يمكنك اختبار واجهات برمجة التطبيقات (APIs) بطريقتين:

🔸 **الخيار 1:**  
نزّل  Postman Collection المرفقة في رابط تسليم المهمة.

- في Postman، اذهب إلى **File > Import**.
- اختر ملف مجموعة Postman.
- استخدم المجموعة المستوردة لاختبار كل نقاط النهاية.

🔸 **الخيار 2:**  
انسخ URLs الموجودة في المشروع بملفات ال urls.py يدويًا واختبرها عبر Postman بعد الحصول على توكن تسجيل الدخول.

---

### ✅ واجهات المهام (محميّة بالتوكن)

| اسم الواجهة                              | الرابط                                              | الطريقة  | الوصف                                                         |
|:---------------------------------------|:----------------------------------------------------|:---------|:--------------------------------------------------------------|
| **واجهة المهام المتزامنة**               | `127.0.0.1:8000/api/tasks/no-scatter-gather/`       | `GET`    | استرجاع المهام والإحصائيات بشكل متسلسل                         |
| **واجهة المهام Scatter-Gather**          | `127.0.0.1:8000/api/tasks/scatter-gather/`          | `GET`    | استخدام نمط Scatter-Gather (تنفيذ غير متزامن ومتوازي) لاسترجاع المهام بالتوازي |

**ملاحظة:**  
كلا واجهتي المهام محميتين وتتطلبان تمرير توكن JWT صالح في رؤوس الطلب.

**ملاحظة:**  
يمكنك اختبار واجهة Scatter-Gather عبر Postman كما تفعل مع أي API آخر، باستخدام المجموعة المرفقة أو الروابط أعلاه.

---

## ⚙️ التقنيات المستخدمة

- Python 3.12  
- Django 5  
- Django REST Framework  
- PostgreSQL  
- ASGI (لدعم غير المتزامن)  
- asyncio, asgiref  

---

