//describe("BDD example", function () {
//  //Runs once before all tests start.
//  before(function () {
//    this.hello = function () {
//      return "Hello World!";
//    };
//  });
//
//  //Runs once when all tests finish.
//  after(function () {
//    this.hello = null;
//  });
//
//  it("should return expected string result", function () {
//    expect(this.hello()).to
//    .be.a("string").and
//    .equal("Hello World!");
//  });
//});



suite("TDD example", function () {
  //Runs once before all tests start.
  suiteSetup(function () {
    this.hello = function () {
      return "Hello World!";
    };
  });

  //Runs once when all tests finish.
  suiteTeardown(function () { 
    this.hello = null;
  });

  test("expected string result", function () {
    assert.isString(this.hello());
    assert.strictEqual(this.hello(), "Hello World!");
  });
});