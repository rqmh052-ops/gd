# Free-Fire-level-up-Xcode (Railway)

تشغيل على Railway:
1. ارفع المشروع على GitHub (Private) وأنشئ مشروع Railway منه.
2. Variables: `DASHBOARD_PASSWORD` (إجباري عملياً)، و`DASHBOARD_USER` (اختياري، الافتراضي admin).
3. أضف Volume (Mount path مثل `/data`) حتى لا تضيع الحسابات والتوكنات عند كل نشر.
4. Settings > Networking > Generate Domain، وافتح الرابط وأضف الحسابات من اللوحة.

متغيرات اختيارية: `DATA_DIR` (مكان الملفات؛ يؤخذ تلقائياً من الـ Volume)، `PORT` (يمرره Railway).
