// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

contract Setter{
    string public name;

    function getName ()
    public
    returns (string memory)
    {
        name = "alex";
        return name;
    }

    function setName (string memory _name)
    public
    returns (string memory)
    {
        name = _name;
        return name;
    }
}