#include <iostream>

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int data) {
        this->data = data;
        left = right = nullptr;
    }
};

void bfs(Node* root) {
    // Create a queue for BFS
    Node** queue = new Node*[100];
    int head = 0;
    int tail = 0;

    // Push the root node to the queue
    queue[tail++] = root;

    // Run while there are nodes in the queue
    while (head < tail) {
        // Get the next node in the queue
        Node* node = queue[head++];

        // Print the data of the node
        std::cout << node->data << " ";

        // Add the left and right children of the node to the queue, if they exist
        if (node->left) {
            queue[tail++] = node->left;
        }
        if (node->right) {
            queue[tail++] = node->right;
        }
    }

    delete[] queue;
}

int main() {
    // Example usage:
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    bfs(root);
    return 0;
}
