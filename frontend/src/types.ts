/**
 * Global Type Definitions for Voter Data
 * Used to ensure data consistency across the React frontend and Python backend.
 */

export interface Voter {
  id: string;
  name: string;
  demographics: string;
  lastContacted?: string; // Optional field
}

export interface AIStrategyResponse {
  voter_id: string;
  strategy: string;
  status?: string;
}