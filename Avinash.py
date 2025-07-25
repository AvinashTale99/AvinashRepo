def introduction():
    name = "Avinash Anant Tale"
    experience = "2 years"
    cloud_skills = ["AWS Cloud", "DevOps"]
    devops_tools = ["Jenkins", "Docker", "Terraform"]

    print("👋 Hello!")
    print(f"My name is {name}.")
    print(f"I have {experience} of working experience in IT.")
    print("I have knowledge of the following domains and tools:")

    print("\n🌩️ Cloud & DevOps:")
    for skill in cloud_skills:
        print(f"- {skill}")

    print("\n🛠️ Tools & Technologies:")
    for tool in devops_tools:
        print(f"- {tool}")

    print("\nLooking forward to exploring more and growing in the DevOps & Cloud field!")

# Run the function
introduction()
