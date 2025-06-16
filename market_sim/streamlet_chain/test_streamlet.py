from protocol import StreamletProtocol

def run_simulation(num_epochs=5, num_nodes=4):
    print("🚀 Starting Streamlet Protocol Simulation")
    protocol = StreamletProtocol(num_nodes=num_nodes)

    for epoch in range(num_epochs):
        print(f"\n⏳ Epoch {epoch}")
        protocol.run_epoch(data=f"transaction_batch_{epoch}")

    # Show blockchains for each node
    print("\n📦 Final Blockchains:")
    for i, node in enumerate(protocol.nodes):
        print(f"\n🧠 Node {i}:")
        for block in node.blockchain:
            print(f"  {block}")

if __name__ == "__main__":
    run_simulation()
