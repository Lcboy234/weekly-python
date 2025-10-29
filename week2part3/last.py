def person(age):
    print("I am a person")
    def student(degree):
        print("I like learning")
        def holiday(place):
            print("But I need to take holidays")
            print(age,"|",degree,"|",place)
        return holiday
    return student

print(person(12)("Math")("beach"))