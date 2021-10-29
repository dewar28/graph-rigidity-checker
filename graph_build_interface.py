import sys
import os
import pygame
from vertices import Vertex
from rigidity_checker import GlobalRigidityChecker

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


class GraphBuilder:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_color = (230, 230, 230)

        self.vertices = pygame.sprite.Group()

        self.graph = GlobalRigidityChecker({}, 2)

        self.new_edge = set()

        self.remove_edge = set()

        pygame.display.set_caption("Rigidity Checker")

    def run_game(self):
        """Start the main loop of the game."""
        print("\nWelcome to Rigidity Checker!")
        print("Instructions:")
        print("1. Click to place a vertex.")
        print("2. Press space when mouse is over vertex to begin an edge, "
              "and press again over another vertex to connect them by an edge.")
        print("3. Delete edges by pressing backspace when the mouse is over the first endpoint, "
              "then again when it is over the second endpoint.")
        print("4. Press c to cancel drawing/deleting an edge.")
        print("5. Press r to check rigidity in 2D, and press g to check global rigidity in 2D.")
        print("6. Use the up and down keys to change the dimension (dimension is currently set to 2).")
        print("7. Press l to get the approximate Laplacian eigenvalues "
              "and press a to get the approximate adjacency matrix eigenvalues.")
        print("8. Press w to reset everything.")
        while True:
            self._check_events()

            self._update_screen()

    def _check_events(self):
        """We are asking it to watch keyboard and mouse commands."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"\nAdjacency list: {self.graph.adjacency_list}.")
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_click(event, mouse_pos)
            elif event.type == pygame.KEYDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_keydown_events(event, mouse_pos)

    def _check_keydown_events(self, event, mouse_pos):
        """Responds when button is pressed."""
        if event.key == pygame.K_q:
            print(f"\nAdjacency list: {self.graph.adjacency_list}.")
            sys.exit()
        elif event.key == pygame.K_SPACE:
            for vertex in self.vertices:
                vertex_clicked = vertex.rect.collidepoint(mouse_pos)
                if vertex_clicked:
                    self.new_edge.add(vertex.name)
            if len(self.new_edge) == 2:
                self.graph.add_edge(self.new_edge)
                self.new_edge = set()
                print(f"\nAdjacency list: {self.graph.adjacency_list}.")
            elif len(self.new_edge) > 2:
                self.new_edge = set()
        elif event.key == pygame.K_BACKSPACE:
            for vertex in self.vertices:
                vertex_clicked = vertex.rect.collidepoint(mouse_pos)
                if vertex_clicked:
                    self.remove_edge.add(vertex.name)
            if len(self.remove_edge) == 2:
                self.graph.delete_edge(self.remove_edge)
                self.remove_edge = set()
                print(f"\nAdjacency list: {self.graph.adjacency_list}.")
            elif len(self.remove_edge) > 2:
                self.remove_edge = set()
        elif event.key == pygame.K_c:
            self.new_edge = set()
            self.remove_edge = set()
        elif (event.key == pygame.K_r) and self.graph.adjacency_list and self.graph.edge_list():
            self.graph.rigidity_check()
        elif event.key == pygame.K_g and self.graph.adjacency_list and self.graph.edge_list():
            self.graph.global_rigidity_check()
        elif event.key == pygame.K_l and self.graph.adjacency_list and self.graph.edge_list():
            print(f"\nThe Laplacian matrix eigenvalues are:\n{self.graph.laplacian_eigenvalues()}.")
        elif event.key == pygame.K_a and self.graph.adjacency_list and self.graph.edge_list():
            print(f"\nThe adjacency matrix eigenvalues are:\n{self.graph.adjacency_eigenvalues()}.")
        elif event.key == pygame.K_DOWN:
            if self.graph.dimension > 1:
                self.graph.dimension_decrease()
                print(f"\nDimension: {self.graph.dimension}.")
        elif event.key == pygame.K_UP:
            self.graph.dimension_increase()
            print(f"\nDimension: {self.graph.dimension}.")
        elif event.key == pygame.K_w:
            d = self.graph.dimension
            self.vertices = pygame.sprite.Group()
            self.graph = GlobalRigidityChecker({}, d)
            self.new_edge = set()
            self.remove_edge = set()
            print(f"\nGraph reset.\nDimension: {self.graph.dimension}.")

    def _check_mouse_click(self, event, mouse_pos):
        if event.button == 1:  # Left click
            mouse_pos_x = mouse_pos[0]
            mouse_pos_y = mouse_pos[1]
            self._create_vertex(mouse_pos_x, mouse_pos_y)

    def _create_vertex(self, mouse_pos_x, mouse_pos_y):
        # Create a vertex and place it correctly.
        vertex = Vertex(self)
        vertex.name = len(self.vertices)
        self.graph.add_vertex()
        vertex.rect.x = mouse_pos_x - vertex.size / 2
        vertex.rect.y = mouse_pos_y - vertex.size / 2

        self.vertices.add(vertex)

    def _update_screen(self):
        """Update images on screen and flip to new screen."""
        self.screen.fill(self.bg_color)

        for vertex in self.vertices:
            vertex.draw_vertex()

        for edge in self.graph.edge_list():
            for vertex_1 in self.vertices:
                for vertex_2 in self.vertices:
                    if edge == {vertex_1.name, vertex_2.name}:
                        pygame.draw.line(self.screen, (0, 0, 0),
                                         (vertex_1.rect.x + vertex.size / 2, vertex_1.rect.y + vertex.size / 2),
                                         (vertex_2.rect.x + vertex.size / 2, vertex_2.rect.y + vertex.size / 2), 10)

        # Make most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    gb = GraphBuilder()
    gb.run_game()
