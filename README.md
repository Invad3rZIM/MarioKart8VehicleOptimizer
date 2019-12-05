# MarioKart8VehicleOptimizer

I made this for my girlfriend so that we can beat MarioKart8 for Nintendo Switch.

This is part 1, a python program that parses html data ripped from a get request and formats it into
the following schema

Part 2 is going to be writing a frontend for it! This will be done in ReactJS

```
name,speed,acceleration,weight,handling,traction/grip,mini-turbo,total
characters
Baby Peach, Baby Daisy,2.25,4.0,2.0,5.0,4.25,4.0,21.5
Baby Rosalina, Lemmy Koopa,2.25,4.25,2.0,4.75,3.75,4.0,21.0
Baby Mario/Luigi, Dry Bones,2.5,4.25,2.0,4.5,4.0,3.75,21.0
Koopa Troopa, Lakitu, Bowser Jr.,2.75,4.0,2.5,4.5,4.25,3.75,21.75
Toadette, Wendy, Isabelle,2.75,4.25,2.5,4.25,3.5,3.75,21.0
Toad, ShyGuy, Larry,3.0,4.0,2.75,4.25,4.0,3.5,21.5
Cat Peach, Inkling Girl, Villager Girl,3.25,4.0,2.75,4.0,3.75,3.5,21.25
Peach, Daisy, Yoshi,3.5,3.75,3.0,3.75,3.75,3.5,21.25
Tanooki Mario, Inkling Boy, Villager Boy,3.5,3.75,3.25,3.75,3.25,3.5,21.0
Luigi, Iggy,3.75,3.5,3.5,3.75,3.25,3.25,21.0
Mario, Ludwig,3.75,3.5,3.5,3.5,3.5,3.25,21.0
Link, King Boo, Rosalina,4.0,3.25,3.75,3.25,3.75,3.25,21.25
Donkey Kong, Roy, Waluigi,4.5,3.25,4.0,3.0,3.0,3.0,20.75
Wario, Dry Bowser,4.75,3.0,4.25,2.75,3.25,2.75,20.75
Metal/Gold Mario, Pink Gold Peach,4.25,3.25,4.5,3.25,3.25,3.0,21.5
Bowser, Morton,4.75,3.0,4.5,2.5,3.0,2.75,20.5
karts
Standard Kart,0,0,0,0,0,0,0
Pipe Frame,-0.5,0.5,-0.25,0.5,0.25,0.5,1.0
Mach 8,0,-0.25,0.25,-0.25,0.25,0,0.0
Cat Cruiser,-0.25,0.25,0,0.25,0,0.25,0.5
Steel Driver,0.25,-0.75,0.5,-0.5,0,-0.5,-1.0
Circuit Special,0.5,-0.75,0.25,-0.5,-0.5,-0.75,-1.75
Tri-Speeder,0.25,-0.75,0.5,-0.5,0,-0.5,-1.0
Badwagon,0.5,-1.0,0.5,-0.75,0.5,-1.0,-1.25
Prancer,0.25,-0.5,-0.25,0,-0.25,-0.25,-1.0
Biddybuggy,-0.75,0.75,-0.5,0.5,0.5,0.25,0.75
Landship,-0.5,0.5,-0.5,-0.5,0.75,0.5,0.25
Sneeker,0.25,-0.5,0,0,-0.75,-0.25,-1.25
Sports Coupe,0,-0.25,0.25,-0.25,0.25,0,0.0
Gold Standard,0.25,-0.5,0,0,-0.75,-0.25,-1.25
Mercedes GLA,0.5,-1.0,0.5,-0.75,0.5,-1.0,-1.25
Mercedes Silver Arrow,-0.25,0.25,-0.25,0.25,0.5,0.25,0.75
Mercedes 300 SL Roadster,0,0,0,0,0,0,0
Blue Falcon,0.25,-0.25,-0.5,-0.25,0.5,0,-0.25
Tanooki Kart,-0.25,-0.5,0.25,0.25,0,1.0,0.75
B Dasher,0.5,-0.75,0.25,-0.5,-0.25,-0.5,-1.25
Streetle,-0.5,0.5,-0.5,-0.5,-0.25,0.75,-0.5
P-Wing,0.5,-0.75,0.25,-0.5,-0.25,-0.5,-1.25
Koopa Clown,-0.25,-0.5,0.25,0.25,0,1.0,0.75
Standard Bike,-0.25,0.25,-0.25,0.25,0.5,0.25,0.75
Comet,-0.25,0.25,0,0.25,0,0.25,0.5
Sport Bike,0.25,-0.5,-0.25,0,-0.25,-0.25,-1.0
The Duke,0,0,0,0,0,0,0
Flame Rider,-0.25,0.25,-0.25,0.25,0.5,0.25,0.75
Varmint,-0.5,0.5,-0.25,0.5,0.25,0.5,1.0
Mr. Scooty,-0.75,0.75,-0.5,0.5,0.25,0.75,1.0
Jet Bike,0.25,-0.5,-0.25,0,-0.25,-0.25,-1.0
Yoshi Bike,-0.25,0.25,0,0.25,0,0.25,0.5
Master Cycle,0.25,-0.5,0,0,-0.75,-0.25,-1.25
City Tripper,-0.5,0.5,-0.25,0.5,0.25,0.5,1.0
Standard ATV,0.5,-1.0,0.5,-0.75,0.5,-1.0,-1.25
Wild Wiggler,-0.25,0.25,-0.25,0.25,0.5,0.25,0.75
Teddy Buggy,-0.25,0.25,0,0.25,0,0.25,0.5
Bone Rattler,0.25,-0.75,0.5,-0.5,0,-0.5,-1.0
Inkstriker,0,-0.25,0.25,-0.25,0.25,0,0.0
Splat Buggy,0.25,-0.25,-0.5,-0.25,0,-0.25,-1.0
tires
Standard,0,0,0,0,0,0,0
Monster,0,-0.5,0.5,-0.75,0.5,-0.25,-0.5
Roller,-0.5,0.5,-0.5,0.25,-0.25,0.75,0.25
Slim,0.25,-0.5,0,0.25,-1.0,-0.25,-1.25
Slick,0.5,-0.75,0.25,-0.25,-1.25,-0.75,-2.25
Metal,0.5,-1.0,0.5,-0.25,-0.75,-0.75,-1.75
Button,-0.25,0.25,-0.5,0,-0.5,0.5,-0.5
Off-Road,0.25,-0.25,0.25,-0.5,0.25,-0.5,-0.5
Sponge,-0.25,0,-0.25,-0.25,0.25,0.25,-0.25
Wood,0.25,-0.5,0,0.25,-1.0,-0.25,-1.25
Cushion,-0.25,0,-0.25,-0.25,0.25,0.25,-0.25
Blue Standard,0,0,0,0,0,0,0
Hot Monster,0,-0.5,0.5,-0.75,0.5,-0.25,-0.5
Azure Roller,-0.5,0.5,-0.5,0.25,-0.25,0.75,0.25
Crimson Slim,0.25,-0.5,0,0.25,-1.0,-0.25,-1.25
Cyber Slick,0.5,-0.75,0.25,-0.25,-1.25,-0.75,-2.25
Retro Off-Road,0.25,-0.25,0.25,-0.5,0.25,-0.5,-0.5
Gold Tires,0.5,-1.0,0.5,-0.25,-0.75,-0.75,-1.75
GLA Tires,0,0,0,0,0,0,0
Triforce Tires,0.25,-0.25,0.25,-0.5,0.25,-0.5,-0.5
Leaf Tires,-0.25,0.25,-0.5,0,-0.5,0.5,-0.5
gliders
Super Glider,0,0,0,0,0,0,0
Cloud Glider,-0.25,0.25,-0.25,0,0,0.25,0.0
Wario Wing,0,0,0.25,0,-0.25,0,0.0
Waddle Wing,0,0,0,0,0,0,0
Peach Parasol,-0.25,0.25,-0.25,0,0,0.25,0.0
Parachute,-0.25,0.25,-0.25,0,0,0.25,0.0
Parafoil,-0.25,0.25,0,0,-0.25,0.25,0.0
Flower Glider,-0.25,0.25,-0.25,0,0,0.25,0.0
Bowser Kite,-0.25,0.25,0,0,-0.25,0.25,0.0
Plane Glider,0,0,0.25,0,-0.25,0,0.0
MKTV Parafoil,-0.25,0.25,0,0,-0.25,0.25,0.0
Gold Glider,0,0,0.25,0,-0.25,0,0.0
Hylian Kite,0,0,0,0,0,0,0
Paper Glider,-0.25,0.25,-0.25,0,0,0.25,0.0
end
```