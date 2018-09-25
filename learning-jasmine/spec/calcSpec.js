describe("Calculator", function() {
    var calc;
    
    beforeEach(function() {
        calc = new Calculator();    
    })
    
    describe("Addition function", function() {
        it("should take two arguments and return the sum of those arguments", function() {
            calc.add(2);
            calc.add(2);
            expect(calc.value).toBe(4);
        });

        it("should not return 4 if the arguments does not sum 4", function() {
            calc.add(7);
            calc.add(19);
            expect(calc.value).toBe(26);
        });

        it("should have called the alert function if either number is undefined", function() {
            spyOn(window, "alert");
            calc.add("Hello");
            expect(window.alert).toHaveBeenCalledWith("Argument must be a number");
        })
    })
})
