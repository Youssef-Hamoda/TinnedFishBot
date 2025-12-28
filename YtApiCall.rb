#!/usr/bin/ruby

require 'rubygems'
gem 'google-api-client', '>0.7'
require 'google/api_client'
require 'json'

config = JSON.parse(File.read('config.json'))

DEVELOPER_KEY = config['yt_api_key']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_service
  client = Google::APIClient.new(
    :key => DEVELOPER_KEY,
    :authorization => nil,
    :application_name => $PROGRAM_NAME,
    :application_version => '1.0.0'
  )
  youtube = client.discovered_api(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION)

  return client, youtube
end

def main

  client, youtube = get_service

  begin
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = client.execute!(
      :api_method => youtube.search.list,
      :parameters => {
        :part => 'snippet',
        :channelId => 'UCnM8PMUe_Kmp4-Ohq4V7Vdw',
        :maxResults => 25,
        :videoDuration => 'short',
        :order => 'rating'
      }
    )

    videos = []

    search_response.data.items.each do |search_result|
        videos << "#{search_result.id.videoId}"
    end

    puts JSON.generate(videos)
    
    rescue Google::APIClient::TransmissionError => e
        e.result.body
    end
end

main