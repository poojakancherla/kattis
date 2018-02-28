package com.company;

public class GetterSetter
{

    private int age;
    private String name;
    String school = "MST";

    public void setName(String name)
    {
        this.name = name;
    }
    public String getName()
    {
        return name;
    }

    public void setAge(int age)
    {
        this.age = age;
    }
    public int getAge()
    {
        return age;
    }

    public static void main(String[] args) {

        GetterSetter gs = new GetterSetter();
        System.out.println(gs.name = "Pooja");
        gs.setAge(12);
        System.out.println(gs.age);
        System.out.println(gs.school);


    }
}
