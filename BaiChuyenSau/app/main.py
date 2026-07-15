from fastapi import FastAPI

app = FastAPI()

@app.post("/enrollments")
def create_enrollment():
    return {"message": "API đăng ký khóa học"}

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):
    return {"message": f"API xem khóa học của sinh viên {student_id}"}



# Sơ đồ quan hệ thực thể (ERD)
# Trong hệ thống quản lý khóa học, ta có 3 bảng chính:
# Student
# Một sinh viên có thể đăng ký nhiều khóa học.

# Course
# Một khóa học có thể có nhiều sinh viên đăng ký.

# Enrollment (bảng trung gian)
# Lưu thông tin đăng ký, kết nối giữa Student và Course.

# Quan hệ: Student (1-N) Enrollment (N-1) Course  
# -> Từ đó tạo thành quan hệ N-N giữa Student và Course thông qua Enrollment.



# Vị trí đặt Khóa ngoại (Foreign Key)
# Bảng Enrollment là bảng con (Child Table).
# Nó phải chứa khóa ngoại:
# student_id -> trỏ đến students.id
# course_id -> trỏ đến courses.id

# Lý do:
# Enrollment chỉ tồn tại khi có Student và Course.
# Nếu không có FK, có thể chèn dữ liệu rác (ví dụ: student_id=999 không tồn tại).
# FK đảm bảo tính toàn vẹn dữ liệu: mỗi bản ghi đăng ký luôn hợp lệ.




# Cơ chế đồng bộ ORM (back_populates)
# Ý nghĩa:
# back_populates tạo liên kết hai chiều:
# Student.enrollments <-> Enrollment.student
# Course.enrollments <-> Enrollment.course

# Nhờ đó:
# Từ một student, có thể truy cập nhanh danh sách courses.
# Từ một course, có thể truy cập nhanh danh sách students.