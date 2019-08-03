using System;
using Grpc.Core;
using Sample;

namespace gRPCSample
{
    class Program
    {
        static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);
            var client = new UserService.UserServiceClient(channel);

            var reply = client.SetUser(new User { Id = 100, Name = "foo" });
            Console.WriteLine(reply.Result);

            channel.ShutdownAsync().Wait();
        }
    }
}
