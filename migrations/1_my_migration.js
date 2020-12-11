const Setter = artifacts.require("Setter");

module.exports = async function (deployer) {
    // deploy  Setter contract
    console.log('try to deploy Setter')
    await deployer.deploy(Setter );
    const setter = await Setter.deployed();

    console.log('\n > Setter deployment succes -->' , Setter.address);

    const addresses = {
        setter: setter.address
      };

};
