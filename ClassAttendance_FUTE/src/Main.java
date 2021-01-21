import attendance.Course;
import attendance.CourseSchedule;
import attendance.Instructor;
import attendance.Student;

import java.util.ArrayList;
import java.util.Date;

public class Main {
	
	public static void main(String args[]) {
		System.out.println("Registering Instructor....");
		Instructor instructor = new Instructor("Dr Fute");
		System.out.println(instructor);
		
		System.out.println("Creating course....");
		Course course1 = new Course("Advanced OOP", "CEF 691", instructor);
		System.out.println(course1);
		
		System.out.println("Creating course schedule....");
		CourseSchedule schedule = new CourseSchedule(course1, new Date(), "CEF LAB");
		System.out.println(schedule);
		course1.addSchedule(schedule);
		
		System.out.println("Registering students....");
		ArrayList<Student> students = new ArrayList<>();
		for (int i = 0; i < 20; i++) {
			students.add(new Student("Student " + (i + 1)));
		}
		course1.setEnrolledStudents(students);
		
		
		System.out.println("Taking Attendance....\n\n");
		for (Student student : students) {
			int rand = (int) (Math.random() * (10 - 1 + 1) + 1);
			
			if (rand % 2 == 0) {
				instructor.takeAttendance(student, schedule);
			}
		}
		
		schedule.generateReport();
	}
}
