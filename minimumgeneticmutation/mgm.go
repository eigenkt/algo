package main

type GeneBank map[string]bool

var startingGene string = "AACCGGTT"
var targetGene string = "AAACGGTA"
var Bank = []string{"AACCGGTA", "AACCGCTA", "AAACGGTA"}

// minMutation will find minimum number of mutations transform the starting gene sequence into the target sequence
func minMutation(startGene string, endGene string, bank []string) int {
	bankSet := make(GeneBank)
	for _, gene := range bank {
		bankSet[gene] = true
	}
	if !bankSet[endGene] {
		return -1
	}
	visited := make(GeneBank)
	visited[startGene] = true
	return bfs(startGene, endGene, bankSet, bankSet)
}

// bfs performs a breadth-first search to find the minimum number of mutations necessary
func bfs(currGene string, endGene string, bankSet GeneBank, visited GeneBank) int {
	queue := []string{currGene}
	mutationCount := 0

	for len(queue) > 0 {
		for i := 0; i < len(queue); i++ {
			currentGene := queue[0]
			queue = queue[1:]

			if currentGene == endGene {
				return mutationCount
			}

			nextGenes := generateNextGenes(currGene)
			for _, nextGene := range nextGenes {
				if !bankSet[nextGene] || visited[nextGene] {
					continue
				}
				visited[nextGene] = true
				queue = append(queue, nextGene)
			}
		}
		mutationCount++
	}
	return -1
}

// generateNextGenes generates all possible next genes from the current gene by changing one nucleotide at a time
func generateNextGenes(currGene string) []string {
	mutations := []string{"A", "C", "G", "T"}
	nextGenes := make([]string, 0, len(currGene)*4)
	for j := 0; j < len(currGene); j++ {
		for _, mutation := range mutations {
			if mutation == currGene {
				continue
			}
			nextGene := currGene[:j] + string(mutation) + currGene[j+1:]
			nextGenes = append(nextGenes, nextGene)
		}
	}
	return nextGenes
}
