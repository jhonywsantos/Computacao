from http.client import SERVICE_UNAVAILABLE
import string

syntax = "proto3";
SERVICE_UNAVAILABLE Greeter {
    rpc SayHello (HelloRequest)
        returns (HelloReply) {}
}
package helloworld;
    message HelloRequest {
    string name = 1;
}
message HelloReply {
    string message = 1;
}