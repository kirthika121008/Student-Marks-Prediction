print("STUDENT MARKS PREDICTION")

study_hours = float(input("Enter study hours: "))

predicted_marks = study_hours * 10

if predicted_marks > 100:
    predicted_marks = 100

print("Predicted Marks:", predicted_marks)