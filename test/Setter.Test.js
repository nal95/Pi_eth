const { assert } = require('chai');
const Setter = artifacts.require("Setter");

require('chai')
    .use(require('chai-as-promised'))
    .should()


contract('name setter', (
    [
        Alex,
        Bob,
    ]) => {

    before(async () => {
        console.log('initial token deployment');
        setter = await Setter.deployed();
    });

    //test the name, supply and symbol :
    describe('Setter Deployement', async () => {
        it('contract has a name ', async () => {
            const name = await setter.name();
            assert.equal(name, 'alex', 'It was not alex');
        });

        it('can set a name', async () => {
            let name = await setter.name();
            setter.setName("veronique");
            name = await  setter.name();
            assert.equal(name, "veronique", 'It was not veronique ');
        });
    });
});