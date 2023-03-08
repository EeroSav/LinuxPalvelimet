use std::env;

fn main(){
	let args: Vec<String> = env::args().collect();
	println!("I got {:?} usable inputs, they were {:?}", args.len(), &args[0..]);
	println!("Hello {}!", &args[1])
}
