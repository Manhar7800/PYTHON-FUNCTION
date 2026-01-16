student={
    "Ajay":89,
    "Arav":55,
    "jay":667,
    "dev":78
}

d1=dict(filter(lambda student_name:student_name[0].startswith("A"),student.items()))

print(d1)