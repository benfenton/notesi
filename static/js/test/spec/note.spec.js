describe("App.Models.Note", function () {

  it("sets passed attributes", function () {
    var model = new App.Models.Note({
      title: "Grocery List",
      text: "Milk Eggs Coffee"

    });
    model.save();
    expect(model.get("title")).to.equal("Grocery List");
    expect(model.get("text")).to.equal("Milk Eggs Coffee");

  });
});