syntax = "proto3";
service Sender {
rpc sendMessage (Message)
returns (Message) {}
}
package chat;
message Message {
string name = 1;
}